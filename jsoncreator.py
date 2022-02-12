import json

Porsha = [
    {
        "Header":"This resume was generated entirely in Python",
        "name": "Porsha Crystal",
        "place": "Redshore City",
        "phone_number": "+(63) 906 285 5648",
        "mail": "Porsha.sing2@outlook.com",
        "skills": [
            {
                "s1": " - Skilled Computer engineer",
                "s2": " - Experienced at Web application and development",
                "s3": " - Proficient with Microsoft Office",
                "s4": " - Adept in troubleshooting ",
                "s5": " - Proficient in HTML Coding",
            }
        ],
        "pixelrei": "Experiences: ",
        "exp": [
            {
                "top": "Computer Engineer",
                "company": "Redshore tech",
                "dates": "2016-2020",
                "ronan": "     - Supervised and lead a team of 5 junior software engineers during development of a robust upgrade version of company's software applications.",
                "John": "     - Enhanced the application's features to effectively fix the bugs and optimize the overall performance.",
                "Alixes": "     - Utilized Cloud Foundry for efficient building on top of Kubernetes.",
                "Lopres": "     - Efficiently deployed and integrated software engineered by team.",
                "next": "Cyrstal Inc.",
                "next1": "September 2015 to May 2016",
                "next2": "    - Completed maintenance on existing programs",
                "next3": "    - Project management, trained new members and technicians"
            }
        ],
        "educ": "Educational Attainment: ",
        "school": [
            {
                "T": "Tertiary: ",
                "U": "ABC university",
                "Sy": "2009-2015"
            }
        ]
    }
]
 
ali = json.dumps(Porsha, indent = 4)
with open('RESUME.json', 'w') as f:
    f.write(ali)
    f.close()