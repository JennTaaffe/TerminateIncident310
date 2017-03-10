
click(Pattern("IncidentTab.png").similar(0.85))
wait(3)
#add a do while loop depending on the number of incidents.

doubleClick(Pattern("activeInc.png").similar(0.90).targetOffset(23,20)) # change depending on if you are terminating Active Incidents or Future Incidents
wait(10)
dragDrop(Pattern("rightslide.png").similar(0.90),Pattern("1489164466729.png").similar(0.80).targetOffset(-80,1)) #Drag the bottom scrollbar to see the terminate Incident button
click("1489164555911.png") #Terminate the incident
click(Pattern("IncTerm.png").similar(0.80).targetOffset(58,42)) #Acknowledge pop ups
click(Pattern("DynMess.png").similar(0.80).targetOffset(144,43))