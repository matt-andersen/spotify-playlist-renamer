Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vagrant.plugins = ['vagrant-vbguest']

  config.vm.synced_folder "./", "/home/vagrant/project"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory = "4096"
  end

  # Install docker:
  config.vm.provision :docker

  # Install trivy, kubectl, kind:
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    curl -sLS https://get.arkade.dev | sudo sh
    arkade get trivy kubectl kind
    mv /root/.arkade/bin/trivy /root/.arkade/bin/kubectl /root/.arkade/bin/kind /usr/local/bin/
    chmod -R 755 /usr/local/bin/
    kind create cluster
    mkdir /home/vagrant/.kube && kind get kubeconfig > /home/vagrant/.kube/config
    echo "cd /home/vagrant/project" >> /home/vagrant/.bashrc
  SHELL

end
