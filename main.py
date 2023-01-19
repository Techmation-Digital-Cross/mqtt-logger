import sys

from service.log_service import LogService, get_available_apps


def start_application_with_arguments(arg):
    # Destruct the app name and service name from args
    app_name = arg[1]
    app_service_name = arg[2]

    # Create a new service
    service = LogService(app_name)
    service.check_service(app_service_name)
    service.start(app_service_name)


def start_application_in_steps():
    apps = get_available_apps().split(",")
    print("Please select which app do you want to run:")

    # Showing available applications
    for index, app in enumerate(apps):
        print(str(index) + ". " + app)
    app = int(input("Application No : "))

    # Get the available services from application
    services: list[str]
    logService: LogService
    try:
        logService = LogService(apps[app])
        services = logService.get_available_services().split(",")
    except IndexError:
        print("Please type the available number.")
        sys.exit(0)

    # Showing the available services according to application
    print("Please select which service do you want to run:")
    for index, service in enumerate(services):
        print(str(index + 1) + ". " + service)
    service = int(input("Service No : "))

    try:
        service_name = services[service]
    except IndexError:
        print("Please type the available number.")
        sys.exit(0)

    logService.start(service_name)


# Main method for application
def initialize_app():
    # Reading arguments passed from user
    total_arguments = len(sys.argv)

    # Check if arguments match or requirement
    if total_arguments > 2:
        print("Application initialized with arguments")
        start_application_with_arguments(sys.argv)
    else:
        start_application_in_steps()


initialize_app()
