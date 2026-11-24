FROM python:3.12
WORKDIR /student_details
COPY . .
CMD ["python", "Student.py"]
