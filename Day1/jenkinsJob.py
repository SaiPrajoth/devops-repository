# Import necessary modules
from flask import Flask, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# Define Jenkins server and job details
jenkins_url = "http://jenkins-server:8080"  # Replace with your Jenkins server URL
jenkins_job = "example-job"  # Replace with your Jenkins job name

# Define Jenkins authentication credentials if needed
jenkins_username = "your_username"
jenkins_password = "your_password"

# Define a route to trigger the Jenkins job
@app.route('/trigger-job', methods=['POST'])
def trigger_jenkins_job():
    try:
        # Trigger Jenkins job using the Jenkins API
        response = requests.post(
            f"{jenkins_url}/job/{jenkins_job}/build",
            auth=(jenkins_username, jenkins_password),
            headers={'Content-Type': 'application/xml'}
        )

        # Check if the job is triggered successfully
        if response.status_code == 201:
            return jsonify({'message': 'Jenkins job triggered successfully'}), 200
        else:
            return jsonify({'error': 'Failed to trigger Jenkins job'}), 500

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(port=5000)
