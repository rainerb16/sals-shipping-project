#Normal Ground Shipping

def normal_ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.50) + 20
  elif weight > 2 and weight <= 6:
    return (weight * 3) + 20
  elif weight > 6 and weight <= 10:
    return (weight *4) + 20
  else:
    return (weight * 4.75) + 20



#Premium Ground Shipping

premium_ground_shipping = 125.00


#Drone Shipping

def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight > 2 and weight <= 6:
    return weight * 9
  elif weight > 6 and weight <= 10:
    return weight * 12
  else:
    return weight * 14.25



#Final Function

def cheapest_shipping(weight):

  normal = normal_ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)

  if normal < premium and normal < drone:
    return "Normal ground shipping is cheapest and costs " + str(normal) + "."

  elif premium < drone and premium < normal:
    return "Premium shipping is cheapest and costs " + str(premium) + "."

  elif drone < premium and drone < normal:
    return "Drone shipping is cheapest and costs " + str(drone) + "."


print(cheapest_shipping())
