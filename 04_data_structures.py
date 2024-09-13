# Data Structures

#%%
# Tuples : Tuples are immutable sequences, meaning that once a tuple is created, its elements cannot be changed. Tuples are useful for storing fixed collections of items. 
# For example, a tuple can be stored the coordinates of a geographic point (latitude,longitude)
# Tuples you don't want to changed and they are wrapped by parenthesis () 

point = (
    35.6895,
    139.6917
) # Tuple represents a geographic point (latitude, longitude)

# You can access elements in a tuple using indexing:

#%%

latitude = point[0]
longitude = point[1]
print(f"Latitude:{latitude}, Longitude:{longitude}")


# %%
point[-2]
# %%

cities = (("Knoxville", "New york"), ("Nashville", "Chicago"))
# %%
cities[1]

# %%
cities[1][1]

# %%
cities[-2][-1]

# %%

## Lists
## List are changeable, they are wrapped by square brackets []

#Example


# %%
path = [(35.6895,139.6917), 
        (34.0522, -118.2487),
        (51.5074, -0.1278),
] # List of tuples represent a path
# %%
path.append ((48.8566, 2.3522)) # Adding Paris to the path
print("Updates path:", path)
# %%
len(path)

# %%
path.append ((48.8566, 2.3522)) # Adding Paris to the path
print("Updates path:", path)
# %%
len(path)
# %%


path = [(35.6895,139.6917), 
        (34.0522, -118.2487),
        (51.5074, -0.1278) ]
# %%
path.append ((48.8566, 2.3522))

# %%
len(path)
# %%
path[1:2]
# %%
path[1]
# %%
path[0]

# %%
path[2]
# %%

path[1:2]
# %%

path[1:3]
# %%

path[0:1]
# %%

path[1:]
# %%

path[0:1]
# %%

path[0:2]
# %%

path[0:]

# %%
path[:]
# %%

path[-2:0]
# %%
path[-2:]
# %%

path[-3:]
# %%

# SETS 
# Sets are unordered collection of unique elements. Sets are useful when you need to store a collection of items but want to eliminate duplicates. 
# Example, you might want to store a set of unique geographic regions visited during a survey

regions = ["North America", "Europe", "Asia"]
regions = set(regions)
# %%


regions
# %%

# You can add a new region to the set
regions.add("Africa")

print("Updated regions:", regions)# %%

# %%

regions.add("Africa")
print("Updated regions:", regions)
# %%

regions.add("Europe") # Attemping to add a duplicate elements
print("Regions after attempting to add duplicate:", regions)

# %%

#Converting back to list

regions_list = list(regions)
print(regions_list)
# %%

regions_list.append("Asia")
regions_list


# %%

# Dictionaries : Are collections of key-value pairs, where each key is unique. Dictionaries are extremely useful for storing data that is associated with specific identifiers, such as attribute data for geographic features.
# For Example, you can use a dictionary to store attributes of a geospatial features, such as city

# Dictionaries are represents by curly brackets {}

city_attributes = {
    "name": "Tokyo",
    "population": 13929286,
    "coordinates": (35.6895, 139.6917)
} # Dictionary storing attributes of a city





# %%
# Example of complex dictionary

city_attributes["name"]
# %%
city_attributes["population"]


# %%
city_attributes["population"] = 14000000
city_attributes ["population"]

# %%
city_attributes["coordinates"] = (30,-100)
city_attributes


# %%
city_attributes["name"] = city_attributes["name"].title()
city_attributes




# %%
# Example of complex dictionary from ChatGPT 

complex_dict = {
    "personal_info": {
        "name": "Azad Chahal",
        "age": 32,
        "contact": {
            "email": "azadchahalpau@gmail.com",
            "phone": "551-358-2526",
            "social_media": {
                "LinkedIn": "linkedin.com/in/azadchahal",
                "Twitter": "@AzadC"
            }
        },
        "address": {
            "current": {
                "city": "Vancouver",
                "country": "Canada",
                "postal_code": "V6B 1A1"
            },
            "permanent": {
                "city": "Salisbury",
                "country": "USA",
                "postal_code": "21804"
            }
        }
    },
    "education": {
        "PhD": {
            "major": "Agricultural and Biological Engineering",
            "university": "Penn State University",
            "year_completed": 2020,
            "research": {
                "title": "Precision Agriculture Optimization",
                "keywords": ["yield", "efficiency", "drones", "sensors"]
            }
        },
        "MS": {
            "major": "Precision Agriculture",
            "university": "Punjab Agricultural University",
            "year_completed": 2016,
            "thesis": {
                "title": "Impact of IoT in Agriculture",
                "chapters": {
                    "chapter_1": {
                        "title": "Introduction",
                        "page_range": "1-20"
                    },
                    "chapter_2": {
                        "title": "Data Analysis Techniques",
                        "page_range": "21-40"
                    }
                }
            }
        }
    },
    "career": {
        "current_position": {
            "title": "Digital Science Lead",
            "company": "Syngenta Seeds",
            "start_date": "2024-01-01",
            "responsibilities": [
                "Manage digital enablement strategies",
                "Lead greenhouse projects for crop improvement",
                "Collaborate with global teams on digital initiatives"
            ]
        },
        "previous_positions": [
            {
                "title": "Senior Financial Analyst",
                "company": "Perdue Foods",
                "years_worked": 2,
                "projects": [
                    {
                        "name": "Cost Reduction Strategy",
                        "impact": "Saved $1M in operational costs"
                    },
                    {
                        "name": "Supply Chain Optimization",
                        "outcomes": {
                            "reduction_in_time": "15%",
                            "increase_in_profit": "10%"
                        }
                    }
                ]
            },
            {
                "title": "Agribusiness Consultant",
                "company": "Corteva Agriscience",
                "years_worked": 3,
                "projects": [
                    {
                        "name": "Precision Agriculture Pilot",
                        "regions": ["Midwest", "Canada"],
                        "technologies_used": ["Drones", "AI", "IoT"]
                    }
                ]
            }
        ]
    },
    "skills": {
        "technical_skills": {
            "programming_languages": ["Python", "SQL", "R"],
            "tools": ["Power BI", "Excel", "Azure DevOps"],
            "data_analysis_methods": ["ANOVA", "Regression", "Time Series Analysis"]
        },
        "soft_skills": ["Leadership", "Cross-functional Collaboration", "Problem Solving"]
    },
    "real_estate_business": {
        "business_name": "TrueSense Realty",
        "services_offered": {
            "3D Tours": {
                "description": "Live3D Tours for immersive property viewing",
                "pricing": "1% listing fee",
                "target_audience": ["Home Buyers", "Real Estate Investors"]
            },
            "VR Services": {
                "description": "Virtual Reality home viewing",
                "locations_available": ["British Columbia", "Ontario"]
            }
        },
        "digital_marketing": {
            "strategies": [
                {
                    "type": "SEO",
                    "focus_keywords": ["MLS marketing", "branding", "real estate leader"]
                },
                {
                    "type": "Social Media",
                    "platforms": ["Instagram", "LinkedIn", "Facebook"]
                }
            ]
        }
    }
}

# %%
complex_dict["career"]["previous_positions"][0]["projects"][1]["outcomes"]["increase_in_profit"]

# %%



# Complex List
complex_list = [
    {
        "name": "Azad Chahal",
        "roles": [
            {
                "role_name": "Finance",
                "companies": [
                    {"company": "AgReliant Genetics", "location": "Indiana, USA", "year": 2024},
                    {"company": "Perdue Foods", "location": "Maryland, USA", "year": 2024}
                ],
                "skills": [
                    {"skill": "Financial Modeling", "tools": ["Excel", "Power BI", "SQL"]},
                    {"skill": "Business Strategy", "experience_years": 5}
                ]
            },
            {
                "role_name": "Agribusiness",
                "companies": [
                    {"company": "Corteva Agriscience", "location": "USA", "year": 2024},
                    {"company": "BCG", "location": "Global", "year": 2024}
                ],
                "projects": [
                    {"project": "Precision Agriculture", "details": {
                        "technologies": ["Drones", "IoT Sensors", "Data Analytics"],
                        "focus": "Yield Optimization",
                        "team_size": 5
                    }},
                    {"project": "Sustainable Biomass", "details": {
                        "approach": "Carbon Sequestration",
                        "regions": ["USA", "Canada"],
                        "outcomes": ["Increased Efficiency", "Cost Reduction"]
                    }}
                ]
            }
        ],
        "education": {
            "degrees": [
                {"degree": "PhD", "major": "Agricultural and Biological Engineering", "institution": "Penn State University"},
                {"degree": "MS", "major": "Precision Agriculture", "institution": "Punjab Agricultural University"}
            ],
            "certifications": [
                {"certification": "Agile Project Management", "provider": "Scrum Alliance"},
                {"certification": "Data Science", "provider": "Coursera"}
            ]
        }
    },
    {
        "name": "Real Estate",
        "services": [
            {
                "service_name": "3D Property Tours",
                "details": {
                    "offerings": [
                        {"offering": "TrueSense", "features": ["Live3D Tours", "1% Listing Fee"]},
                        {"offering": "VR Services", "regions": ["British Columbia", "Canada"]}
                    ]
                }
            },
            {
                "service_name": "Digital Presence",
                "strategies": [
                    {"strategy": "SEO", "focus": ["Keywords", "Branding", "MLS Marketing Leader"]},
                    {"strategy": "Social Media", "platforms": ["Instagram", "Facebook", "LinkedIn"]}
                ]
            }
        ]
    }
]


# %%
complex_list
# %%
complex_list[0]["role_name"]
# %%
