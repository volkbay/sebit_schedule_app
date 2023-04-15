# sebit_schedule_app
This is a simple application that calculates the number of high school teachers needed for each branch. The data needed are gathered from `main.xlsx` file. School-specific information comes from `list.xlsx` and modified results are printed in `result.xlsx`. 

>**Dependencies** This is a Python3 project using modules `numpy`, `xlrd`, `PySide2`, and `openpyxl`.

The algorithm intelligently considers the following criteria:
- Weekly hours
- Must/elective status (of the courses)
- Persona of the students from each year
- Distribution of the personas
- Number of student

<img src="https://user-images.githubusercontent.com/97564250/232238950-8270f3db-99ae-4515-be42-ec4e81fc0d85.jpg"  width="100%" height="50%">
<p float="left">
  <img src="https://user-images.githubusercontent.com/97564250/232238959-a8e4dc6d-5567-47a0-a9bb-2fb9a1649c32.jpg"  width="72%" >
  <img src="https://user-images.githubusercontent.com/97564250/232238955-703a8f03-eb33-419d-be39-1b68b07ec196.jpg"  width="27.5%" >
</p>

_Figure: (a) Main screen (b) Persona configuration (c) Distribution of personas_

