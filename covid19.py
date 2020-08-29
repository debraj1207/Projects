import requests

url = "https://api.covid19api.com/summary"

response=requests.get(url)
read_data=response.json()
print("*****Covid-19 Cases overview*****")


for i in read_data.keys():
    print("\n\nYour query: \n*For Global data type G\n*For Country wise data type C\n*To Exit type X")
    i= input("\nEnter your choice:")
    if i=="G":
        print("To know about currrent details globally:\n*For New Confirmed Cases type NC \n*For Total Confirmed Cases type TC \n*For Total Deaths Cases type TD")
        g=input("\n\nEnter your choice: ")
        if g=="NC":
            print("\n\nNumber of New Confirmed Cases:" ,read_data["Global"]["NewConfirmed"])
        elif g=="TC":
            print("\n\nNumber of Total Confirmed Cases:",read_data["Global"]["TotalConfirmed"])
        elif g=="TD":
            print("\n\nNumber of Total Deaths Cases:",read_data["Global"]["TotalDeaths"])
    elif i=="C":
        j=0
        q = input("Enter the country name:")
        while(j<=300):
            
            if read_data["Countries"][j]["Country"]==q:
                print("\n\nTo know about currrent details of {}:\n*For New Confirmed Cases type NC \n*For Total Confirmed Cases type TC\n*For New Deaths Cases type ND\n*For Total Deaths Cases type TD\n*For Total Recovered Caces type TR".format(q))
                f=input("\nEnter your choice:")
                if f=="NC":
                    print("\n\nNumber of New Confirmed Cases:" ,read_data["Countries"][j]["NewConfirmed"])
                elif f=="TC":
                    print("\n\nNumber of Total Confirmed Cases:",read_data["Countries"][j]["TotalConfirmed"])
                elif f=="ND":
                    print("\n\nNumber of New Death Cases:",read_data["Countries"][j]["NewDeaths"])
                elif f=="TD":
                    print("\n\nNumber of Total DeathC Cases:",read_data["Countries"][j]["TotalDeaths"])
                elif f=="TR":
                    print("\n\nNumber of Total Recovered Cases:",read_data["Countries"][j]["TotalRecovered"])
                break
            j+=1

    elif i == "X":
        break