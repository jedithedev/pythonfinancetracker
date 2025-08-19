#Imports
import plotly.graph_objects as go
import plotly.io as pio
import json

#"Global" variable
global diagram

#Code to create the graph
def graph():
    global diagram

    with open("finances.json", "r") as f:
        try :
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            print("No data found")
            data = []
            return

    labels = []
    labels.extend(data["income"])
    labels.append("Budget")
    labels.extend(data["expenses"])
    labels.append("Extra")
    
    income_labels = []
    income_labels.extend(data["income"])
    
    expenses_labels = []
    expenses_labels.extend(data["expenses"])
    
    values = []
    values.extend(data["income_volume"])
    values.extend(data["expenses_volume"])
    
    income_values = []
    income_values.extend(data["income_volume"])
    
    expenses_values = []
    expenses_values.extend(data["expenses_volume"])
    
    budget_number = labels.index("Budget")
    sources = []
    targets = []
    values_for_links = []
    total_income = 0
    total_expenses = 0
    bextra = False
    
    income_values = [int(i) for i in income_values]
    expenses_values = [int(i) for i in expenses_values]  
    total_income = sum(income_values)
    total_expenses = sum(expenses_values)
    
    if total_income > total_expenses:
        extra_value = total_income - total_expenses
        bextra = True
    else:
        bextra = False
        
    for i in range(len(income_labels)):
        sources.append(i)
        targets.append(budget_number)
        values_for_links.append(income_values[i])

    for i in range(len(expenses_labels)):
        sources.append(budget_number)
        targets.append(len(income_labels) + i + 1)
        values_for_links.append(expenses_values[i])

    if bextra == True:
        sources.append(budget_number)
        targets.append(len(income_labels) + len(expenses_labels) + 1)
        values_for_links.append(extra_value)
    
    diagram = go.Figure(data=[
        go.Sankey(
            node=dict(
                thickness=15,
                label=labels,
                pad = 15,
                color = "rgba(0,0,0, 0.9)"
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values_for_links,
                color = "rgba(128,128,128, 0.3)"
            )
        )
    ])

    diagram.update_layout(
        title="Elliott and Matthew's finance tracker",
        font=dict(size=30, color='white'),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        hovermode = "closest",
    )

#Code that shows the graph as a photo in graph.png
    with open('graph.png', 'wb') as file:
        file.write(pio.to_image(diagram, format="png", width=1920, height=1080))
    

        #Code to display on a new tab (doesn't work on school internet)
        #diagram.show()

graph()
