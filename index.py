# Hello:
#   Yo: 1
#   Yoo: 2
#
import copy
def handler(event, context):
    fragment = event["fragment"]
    result = copy.deepcopy(fragment)

    if "Hello" in fragment:
        hello = fragment["Hello"]
        del result["Hello"]

        # check input
        assert isinstance(hello, dict)

        if not "Resources" in fragment:
            result["Resources"] = {}
        for name, amount in hello.items():
            for i in range(int(amount)):
                result["Resources"][f"{name}{i}Instance"] = {
                    "Type": "AWS::EC2::Instance",
                    "Properties": {
                        "InstanceType": "t2.micro",
                        "ImageId": "ami-025f4dd341fda0cf6",
                    }
                }
    return {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": result,
    }
