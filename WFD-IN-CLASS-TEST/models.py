from django.db import models

class Car(models.Model):
    carID = models.IntegerField(primary_key=True, name="Car_ID", unique=True)
    serialNumber = models.IntegerField(name="Serial Number")
    make = models.TextField(name="Make")
    model = models.TextField(name="Model")
    colour = models.TextField(name="Colour")
    Year = models.IntegerField(name="Year")
    forSale = models.BooleanField(name="Car for Sale")

class Customer(models.Model):
    customerID = models.IntegerField(name="Customer_ID", primary_key=True, unique=True)
    lastName = models.TextField(name="Last Name")
    firstName = models.TextField(name="First Name")
    # In a text field since phone numbers can have dashes
    phoneNum = models.TextField(name="Phone number")
    address = models.TextField(name="Address")
    city = models.TextField(name="City")
    state = models.TextField(name="state/province")
    country = models.TextField(name="Country")
    postalCode = models.TextField(name="Postal Code")


class Salesperson(models.Model):
    salespersonID = models.IntegerField(primary_key=True, unique=True, name="Salesperson_ID")
    lastName = models.TextField(name="Last Name")
    firstName = models.TextField(name="First Name")

class SalesInvoice(models.Model):
    invoiceID = models.IntegerField(name="Invoice_ID", primary_key=True, unique=True)
    invoiceNum = models.IntegerField(name="Invoice Number")
    carID = models.ForeignKey(Car, name="CarID")
    customerID = models.ForeignKey(Customer, name="Customer ID")
    salespersonID = models.ForeignKey(Salesperson, name="Salesperson ID")

class ServiceTicket(models.Model):
    serviceticketID = models.IntegerField(primary_key=True, unique=True, name="Service_Ticket_ID")
    serviceticketNumber = models.IntegerField(name="Service Ticket Number")
    carID = models.ForeignKey(Car, name="Car ID")
    customerID = models.ForeignKey(Customer, name="Customer ID")
    dateRecv = models.DateTimeField(name="Date Received")
    comments = models.TextField(name="Comments")
    dateRet = models.TimeField(name="Date Returned To Customer")

class Parts(models.Model):
    partsID = models.IntegerField(primary_key=True, unique=True, name="Parts_ID")
    partNum = models.IntegerField(name = "Part Number")
    desc = models.TextField(name = "Description")
    purchasePrice = models.DecimalField(name = "Purchase Price")
    retailPrice = models.DecimalField(name = "Retail Price")

class PartsUsed(models.Model):
    partsusedID = models.IntegerField(name="Parts_Used_ID", primary_key=True, unique=True)
    partID = models.ForeignKey(Parts, name="Part ID")
    serviceticketID = models.ForeignKey(ServiceTicket, name="Service Ticket ID")
    numberUsed = models.IntegerField(name="Number Used")
    price = models.DecimalField(name = "Price")

class Mechanic(models.Model):
    mechanicID = models.IntegerField(name = "Mechanic_ID", primary_key=True, unique=True)
    lastName = models.TextField(name="Last Name")
    firstName = models.TextField(name = "First Name")

class Service(models.Model):
    serviceID = models.IntegerField(name="Service_ID", primary_key=True, unique=True)
    serviceName = models.TextField(name = "Service Name")
    hourlyRate = models.DecimalField(name = "Hourly Rate")

class ServiceMechanic(models.Model):
    serviceMechanicID = models.IntegerField(name = "ServiceMechanic_ID", primary_key=True, unique=True)
    serviceticketID = models.ForeignKey(ServiceTicket, name="Service Ticket ID")
    serviceID = models.ForeignKey(Service, name = "Service ID")
    mechanicID = models.ForeignKey(Mechanic, name="Mechanic ID")
    hours = models.DurationField(name="Hours")
    comment = models.TextField(name="Comment")
    rate = models.DecimalField(name="Rate")