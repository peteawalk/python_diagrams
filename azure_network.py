
from diagrams import Diagram
from diagrams.azure.network.ApplicationGateway
from diagrams.azure.network.VirtualNetworks
from diagrams.azure.integration.APIManagement
from diagrams.azure.integration.LogicApps


with Diagram('Azure APIM and AppGW Implementation (colored)', show=False):
    ingress = Internet("ingress")

    APPGW('LB and WAF') >> VNET('PROD') >> APIM('API Layer') >> LOGICAPP('Compute Layer') 
