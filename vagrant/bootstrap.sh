apt-get update

# Install trivy, kubectl, kind, helm, and flux:
curl -sLS https://raw.githubusercontent.com/alexellis/arkade/0.8.23/get.sh | sudo sh
arkade get trivy kubectl kind helm flux
mv /root/.arkade/bin/trivy \
  /root/.arkade/bin/kubectl \
  /root/.arkade/bin/kind \
  /root/.arkade/bin/helm \
  /root/.arkade/bin/flux \
  /usr/local/bin/
chmod -R 755 /usr/local/bin/

# Create cluster with container registry enabled:
curl -sLS https://kind.sigs.k8s.io/examples/kind-with-registry.sh | sudo sh
mkdir /home/vagrant/.kube && kind get kubeconfig > /home/vagrant/.kube/config
chmod 600 /home/vagrant/.kube/config && chown vagrant: /home/vagrant/.kube/config

# Install Python:
apt-get install python3-venv

echo "cd /home/vagrant/project" >> /home/vagrant/.bashrc
