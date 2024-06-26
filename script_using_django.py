import os
import sys
import django


# Adjust the path to your Django project directory
# django_project_dir = r'E:\DjangoProject\GraphDashboard'
django_project_dir = r'E:\DjangoProject\ToDoApp'
sys.path.append(django_project_dir)

# Set up Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GraphDashboard.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoApp.settings')
django.setup()

# Import your Django models or other components
# from dashboard.models import EmployeeData
from todos.models import ToDo

def main():
    # Your script logic here
    # my_objects = EmployeeData.objects.all()
    objects = ToDo.objects.all()
    for obj in objects:
        # print(f'Found object: {obj}')
        print(f'Found object: {obj.content}-{obj.status}')

if __name__ == "__main__":
    main()