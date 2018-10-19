# coding: utf-8
import boto3
session = boto3.Session(profile_name='default')
ec2 = session.resource
ec2
ec2 = session.resource(ec2)
ec2 = session.resource('ec2')
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_name
key.meta
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
key_path
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S.IWUSR)
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
chmod 400 python_automation_key.pem
chmod _r python_automation_key.pem
chmod +r python_automation_key.pem
chmod 400 python_automation_key.pem
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-0303c7b2e7066b60d')
img
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-0303c7b2e7066b60d')
img_apse2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20181008-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
filters
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
instance = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instance
inst = instance[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst
inst.console_output
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
inst.security_groups
inst.key_name
inst.attach_volume
inst.hypervisor
sg = ec2.SecurityGroup(inst.security_groups[0][GroupId])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '107.204.171.250/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
get_ipython().run_line_magic('save', 'ec2_example.py 1-46')
get_ipython().run_line_magic('save', 'ec2_example.py 1-66')
