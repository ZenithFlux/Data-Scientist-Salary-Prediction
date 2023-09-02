from setuptools import setup, find_packages

def get_requirements():
    lines = []
    with open("requirements.txt", 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if l.startswith(('#','-')) or l=="": continue
            lines.append(l)
    return lines


setup(name="ds_salary_prediction",
      version="0.0.1",
      description="Predict the salaries of a data science professionals",
      author="Chaitanya Lakhchaura",
      license="MIT",
      packages= find_packages(),
      install_requires=get_requirements())