import flask
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def display_resume():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roberto Sanchez's Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ffffff;
            margin: 0;
            padding: 0;
            color: #333333;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background: #ffffff;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        header {
            text-align: center;
            padding: 20px 0;
            background-color: #0073e6;
            color: white;
        }
        header h1 {
            margin: 0;
            font-size: 3rem;
            color: #ffffff;
        }
        header p, header a {
            color: #ffffff;
            margin: 5px 0;
            text-decoration: none;
            font-size: 1.2rem;
        }
        .content-section {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        h2 {
            color: #0073e6;
            margin-top: 0;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Roberto Sanchez</h1>
        <p>Margate, FL 33063 | +1 754 368 1795 | <a href="mailto:robertacos16@gmail.com">robertacos16@gmail.com</a></p>
        <p>GitHub: <a href="https://github.com/Robertacos16">@Robertacos16</a></p>
    </header>
    <div class="container">
        <div class="content-section">
            <h2>Objective</h2>
            <p>A dedicated, focused, and enthusiastic individual aiming to gain tech experience and achieve long-term career goals while pursuing a Master's in Technology Management. Currently preparing for the Security+ certification.</p>
        </div>
        <div class="content-section">
            <h2>Skills</h2>
            <ul>
                <li>Microsoft Excel</li>
                <li>Word</li>
                <li>SQL (3 years)</li>
                <li>CSS3 (Less than 1 year)</li>
                <li>Agile (2 years)</li>
                <li>Technology (3 years)</li>
                <li>Python (2 years)</li>
                <li>Linux (1 year)</li>
                <li>Technical Support (2 years)</li>
                <li>Bilingual (10+ years)</li>
                <li>Database Management and Analysis (1 year)</li>
                <li>Analysis Skills (3 years)</li>
                <li>Power BI (1 year)</li>
                <li>C++ (1 year)</li>
                <li>Jira (1 year)</li>
                <li>Git (1 year)</li>
                <li>AI Prompt Engineering</li>
                <li>Microsoft Office Certified</li>
                <li>Payfactors Certified</li>
            </ul>
        </div>
        <div class="content-section">
            <h2>Education</h2>
            <ul>
                <li><strong>Bachelor of Applied Science in IT and Cybersecurity</strong> - Broward College, FL (Expected June 2026)</li>
                <li><strong>Certificate of Technical Studies in Computer Database & Programming</strong> - Atlantic Technical College, FL (2020)</li>
                <li><strong>High School Diploma</strong> - Atlantic Technical College, FL (2019)</li>
                <li><strong>Certificate of Technical Studies in Automotive Service Technology</strong> - Atlantic Technical College, FL (2019)</li>
            </ul>
        </div>
        <div class="content-section">
            <h2>Work Experience</h2>
            <h3>IT Product Analyst Co-Op - Johnson & Johnson, Palm Beach Gardens, FL (June 2024 - Current)</h3>
            <ul>
                <li>Commissioned, updated, and decommissioned assets in IRIS ITMS and Asset Management databases to generate impactful reports.</li>
                <li>Managed cross-functional projects with Agile methodologies and conducted User Acceptance Testing (UAT).</li>
                <li>Familiarized with the Mendix Low Code Platform for time-efficient development.</li>
                <li>Trained team members on Zollers procedures, monitored project progress, and identified risks to maintain project schedules.</li>
            </ul>
            <h3>Compensation Analyst Intern - JM Family, Deerfield Beach, FL (May 2024 - June 2024)</h3>
            <ul>
                <li>Prepared detailed reports using advanced Excel functions, including Vlookups, Xlookups, and Index matches.</li>
                <li>Collaborated with Product Owners, Compensation team, and HR to manage accurate job-related records in Workday and Payfactors.</li>
            </ul>
            <h3>Data Analyst Intern - City Furniture, Fort Lauderdale, FL (May 2023 - August 2023)</h3>
            <ul>
                <li>Extracted and transformed data using DB2, COGNOS, and DENODO tools for various departments.</li>
                <li>Created Power BI dashboards and ensured data quality through validation procedures.</li>
                <li>Identified opportunities for process optimization and adopted emerging data analysis trends.</li>
            </ul>
        </div>
        <div class="content-section">
            <h2>Certifications</h2>
            <ul>
                <li>Microsoft Office Certified</li>
                <li>Payfactors Certified</li>
            </ul>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)