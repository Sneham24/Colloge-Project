#!/usr/bin/env python3
"""
Simple email sender for Parent Bless booking forms
This script handles form submissions and sends emails directly
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/send_booking_email':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse JSON data
                data = json.loads(post_data.decode('utf-8'))
                
                # Create email content
                subject = f"New Appointment Booking from {data.get('name', 'Unknown')}"
                
                body = f"""
New Appointment Booking Details:

Name: {data.get('name', 'Not provided')}
Gender: {data.get('Gender', 'Not provided')}
Age: {data.get('Age', 'Not provided')}
Email: {data.get('Email', 'Not provided')}
Contact Number: {data.get('Contact', 'Not provided')}
Address: {data.get('Address', 'Not provided')}
Service: {data.get('service', 'Not provided')}
Preferred Date: {data.get('date', 'Not provided')}
Preferred Time: {data.get('time', 'Not specified')}
{data.get('homeMessage', '') and f"Home Service Instructions: {data['homeMessage']}"}
{data.get('message', '') and f"Additional Message: {data['message']}"}

Please contact the patient to confirm the appointment.
                """.strip()
                
                # Send email (for now, just log it)
                print(f"Email would be sent to pbpainreliefhub@gmail.com")
                print(f"Subject: {subject}")
                print(f"Body: {body}")
                
                # Return success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': True,
                    'message': 'Booking submitted successfully!'
                }).encode())
                
            except Exception as e:
                print(f"Error: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'error': str(e)
                }).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, EmailHandler)
    print("Email server running on port 8001...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
