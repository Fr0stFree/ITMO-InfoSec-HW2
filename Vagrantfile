Vagrant.configure("2") do |config|
  config.vm.box = "net9/ubuntu-24.04-arm64"
  config.vm.hostname = "suricata-lab"

  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"
  config.vm.network "forwarded_port", guest: 5636, host: 5636, id: "evebox"
  
  config.vm.provider "virtualbox" do |vb|
    vb.name = "suricata-lab"
    vb.memory = "4096"
    vb.cpus = 2
  end
end