import subprocess
import json


def requirements_analyser(requirements):
    requirements_file = open(requirements, 'r')
    list_requirements = []
    # for i in requirements_file:
    #     list_requirements.append(i.rstrip())
    [list_requirements.append(line.rstrip()) for line in requirements_file]
    requirements_file.close()
    end_requirements_file = ' '.join(list_requirements)
    subprocess.call(f"pip-licenses --format=json --summary --packages {end_requirements_file} >licenses_list.json", shell=True)
    json_file = open('licenses_list.json', 'r')
    json_list = json.load(json_file)
    json_file.close()
    return json_list


def license_comparison():
    json_list = requirements_analyser('requirements.txt')
    for license_dict in json_list:
        for name in license_dict:
            if name == 'License':
                print(license_dict[name])
                if license_dict[name] in 'road':
                    print(license_dict[name])
                else:
                    print('Nope')


if __name__ == '__main__':
    print(requirements_analyser('requirements.txt'))
