from flask import Flask, render_template_string, send_file
import qrcode
import os

app = Flask(__name__)

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roberto Sanchez - Interactive Resume</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        #intro {
            text-align: center;
            padding: 50px;
            background-color: #007bff;
            color: white;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #contact-info {
            position: absolute;
            top: 10px;
            right: 10px;
            text-align: right;
        }
        #contact-info a {
            color: white;
            text-decoration: none;
            margin-left: 10px;
        }
        #intro button {
            background-color: #fff;
            color: #007bff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 1.2em;
            transition: background-color 0.3s;
        }
        #intro button:hover {
            background-color: #f0f0f0;
        }
        #content-container {
            display: flex;
            align-items: center;
            margin-top: 20px;
        }
        #qr-code {
            width: 150px;
            height: 150px;
        }
        .section {
            padding: 20px;
            margin: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .skills-grid {
            display: flex;
            flex-wrap: wrap;
        }
        .skill {
            padding: 10px;
            margin: 5px;
            background-color: #007bff;
            color: #fff;
            border-radius: 5px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div id="intro">
        <div id="contact-info">
            <p>Email: <a href="mailto:robertacos16@gmail.com">robertacos16@gmail.com</a></p>
            <p>Phone: +1 754 368 1795</p>
            <a href="/download-resume" class="download-link">Download Resume <i class="fas fa-download"></i></a>
        </div>
        <h1>Roberto Sanchez</h1>
        <p>Co-Op IT Product Analyst at Johnson & Johnson</p>
        <div id="content-container">
            <img id="qr-code" src="/static/qr_code.png" alt="QR Code to my LinkedIn">
        </div>
        <p>I'm passionate about technology, data analysis, and finding creative solutions to modern business challenges.</p>
        <button id="exploreButton" onclick="revealSections()">Explore My Journey</button>
    </div>

    <section id="experience" class="section hidden">
        <h2>Work Experience</h2>
        <div class="job">
            <h3>Johnson & Johnson - Co-Op IT Product Analyst</h3>
            <p>June 2024 - Present</p>
            <ul>
                <li>Contributed to initiatives in data integration and security.</li>
                <li>Streamlined product processes using agile methodologies.</li>
                <li>Familiarized with the Mendix Low Code Platform for efficient development.</li>
            </ul>
        </div>
        <div class="job">
            <h3>City Furniture - Data Analyst Intern</h3>
            <p>May 2023 - August 2023</p>
            <ul>
                <li>Visualized data using Power BI for key business insights.</li>
                <li>Ensured data quality through validation procedures.</li>
                <li>Improved processes through pattern recognition and collaboration.</li>
            </ul>
        </div>
    </section>

    <section id="education" class="section hidden">
        <h2>Education</h2>
        <p><strong>Bachelor's in Information Technology and Cybersecurity</strong><br>Broward College - Present</p>
        <p><strong>Technical Degree in Database Development & Programming</strong><br>Atlantic Technical College - 2019 to 2020</p>
    </section>

    <section id="skills" class="section hidden">
        <h2>Skills</h2>
        <div class="skills-grid">
            <div class="skill">SQL</div>
            <div class="skill">Agile</div>
            <div class="skill">Python</div>
            <div class="skill">Power BI</div>
            <div class="skill">Git</div>
            <div class="skill">CSS3</div>
        </div>
    </section>

    <section id="contact" class="section hidden">
        <h2>Contact</h2>
        <p><strong>Email:</strong> <a href="mailto:robertacos16@gmail.com">robertacos16@gmail.com</a></p>
        <p><strong>Phone:</strong> +1 754 368 1795</p>
    </section>

    <script>
        function revealSections() {
            const sections = document.querySelectorAll('.section');
            sections.forEach(section => {
                section.classList.remove('hidden');
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def resume():
    # Create 'static' directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # Smaller box size to reduce the overall size of the QR code
        border=2,
    )
    qr.add_data('https://www.linkedin.com/in/roberto-sanchez-551578191/?trk=opento_sprofile_details')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/qr_code.png')

    return render_template_string(html_content)

@app.route('/download-resume')
def download_resume():
    return send_file('Roberto-Sanchez-2024-Final.pdf', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
