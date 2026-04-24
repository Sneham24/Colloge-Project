// Email Service for Parent Bless Website
// This service handles form submissions and sends emails directly

class EmailService {
    constructor() {
        this.serviceUrl = 'https://api.emailjs.com/api/v1.0/email/send';
        this.serviceId = 'service_parentbless'; // You'll need to configure this
        this.templateId = 'template_booking'; // You'll need to configure this
        this.userId = 'user_publickey'; // You'll need to configure this
    }

    async sendBookingEmail(formData) {
        try {
            const emailData = {
                service_id: this.serviceId,
                template_id: this.templateId,
                user_id: this.userId,
                template_params: {
                    from_name: formData.name,
                    from_email: formData.Email,
                    phone: formData.Contact,
                    address: formData.Address,
                    gender: formData.Gender,
                    age: formData.Age,
                    service: formData.service,
                    date: formData.date,
                    time: formData.time || 'Not specified',
                    home_message: formData.homeMessage || '',
                    message: formData.message || '',
                    to_email: 'pbpainreliefhub@gmail.com'
                }
            };

            const response = await fetch(this.serviceUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(emailData)
            });

            if (response.ok) {
                return { success: true, message: 'Booking request sent successfully!' };
            } else {
                throw new Error('Failed to send email');
            }
        } catch (error) {
            console.error('Email service error:', error);
            return { success: false, error: error.message };
        }
    }

    async sendContactEmail(formData) {
        try {
            const emailData = {
                service_id: this.serviceId,
                template_id: 'template_contact', // Different template for contact
                user_id: this.userId,
                template_params: {
                    from_name: formData.name,
                    from_email: formData.Email,
                    phone: formData.Contact,
                    message: formData.message,
                    to_email: 'pbpainreliefhub@gmail.com'
                }
            };

            const response = await fetch(this.serviceUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(emailData)
            });

            if (response.ok) {
                return { success: true, message: 'Contact form submitted successfully!' };
            } else {
                throw new Error('Failed to send email');
            }
        } catch (error) {
            console.error('Email service error:', error);
            return { success: false, error: error.message };
        }
    }

    // Fallback method using Formspree (alternative)
    async sendViaFormspree(formData, formType) {
        try {
            const formspreeUrl = 'https://formspree.io/f/xyz123'; // You'll need to create a Formspree form
            
            const response = await fetch(formspreeUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    ...formData,
                    form_type: formType,
                    _subject: formType === 'booking' ? 
                        `New Appointment Booking from ${formData.name}` : 
                        `New Contact Enquiry from ${formData.name}`
                })
            });

            if (response.ok) {
                return { success: true, message: 'Form submitted successfully!' };
            } else {
                throw new Error('Failed to submit form');
            }
        } catch (error) {
            console.error('Formspree error:', error);
            return { success: false, error: error.message };
        }
    }
}

// Export for use in HTML files
window.EmailService = EmailService;
