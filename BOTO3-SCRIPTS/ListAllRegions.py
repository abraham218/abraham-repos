import boto3
client = boto3.client('ec2')
regions = client.describe_regions().get('Regions',[] )

def instanceList():
    for region in regions:
        listRegions = list(region['RegionName'].split(" "))
        #print(listRegions)
        for region_name in listRegions:
            ec2= boto3.resource('ec2', region_name=region_name)
            instances= ec2.meta.client.describe_instances()
            for instance in instances['Reservations']:
                print(f"Region : {listRegions} Instance : {instance} ")
                #print(instance)

if __name__ == "__main__":
    #print("Listing Instances in all Regions ")
    instanceList()






