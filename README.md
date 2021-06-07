# ML_Model_on_Docker



Steps to follow:
* Check docker service is running or not...(Docker should be installed in the BaseOS)
    Command: systemctl status docker 
* Pull an image containing any os (I am using CentOS)
    Command: docker pull centos
* Start the container using that image
    Command: docker run -it -name salary_predictor centos
* We have to copy required files inside the container(I am cloning it from here itself)
    Command: git clone  repo url
* Install Python & required libraries for ML model
    Commands: - yum install python3
                pip3 install joblib
                pip3 install scikit-learn
                pip3 install pandas
* Run the Predictor file
