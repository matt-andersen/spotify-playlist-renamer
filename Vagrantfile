Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vagrant.plugins = ['vagrant-vbguest']

  config.vm.synced_folder "./", "/home/vagrant/project"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory = "8192"
  end

  config.vm.provision :docker

  config.vm.provision :shell, path: "bootstrap.sh"

end
