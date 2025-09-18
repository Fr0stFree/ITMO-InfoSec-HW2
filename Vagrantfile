Vagrant.configure("2") do |config|
  config.vm.box = "net9/ubuntu-24.04-arm64"
  config.vm.hostname = "suricata-lab"
  config.vm.synced_folder ".", "/home/vagrant/suricata-lab"

  config.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correct: true
  config.vm.network "private_network", ip: "192.168.56.101"
  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"
  
  config.vm.provider "virtualbox" do |vb|
    vb.name = "suricata-lab"
    vb.memory = "4096"
    vb.cpus = 2
  end
end