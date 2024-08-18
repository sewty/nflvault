```dataview
table
	AtoZRankings[0].ovr as "2024 OVR",
	AtoZRankings[1].hc as "2024 HC",
	AtoZRankings[2].offense as "2024 OFF",
	AtoZRankings[3].oc as "2024 OC",
	AtoZRankings[4].qb as "2024 QB",
	AtoZRankings[5].rb as "2024 RB",
	AtoZRankings[6].wr as "2024 WR",
	AtoZRankings[7].te as "2024 TE",
	AtoZRankings[8].ol as "2024 OL",
	AtoZRankings[9].defense as "2024 DEF",
	AtoZRankings[10].dc as "2024 DC",
	AtoZRankings[11].edge as "2024 EDGE",
	AtoZRankings[12].dl as "2024 IDL",
	AtoZRankings[13].lb as "2024 LB",
	AtoZRankings[14].cb as "2024 CB",
	AtoZRankings[15].safety as "2024 Safety",
	bootleg[0].qbs as "2023 QBS",
	bootleg[1].pwr as "2023 PWR",
	bootleg[2].rusho as "2023 RushO",
	bootleg[3].passo as "2023 PassO",
	bootleg[4].rushd as "2023 RushD",
	bootleg[5].passd as "2023 PassD",
	bootleg[6].pf as "2023 Points For",
	bootleg[7].pa as "2023 Points Allowed",
	bootleg[8].pdiff as "2023 Points Diff"
from "notes/2024-2025/Power Rankings/Team Power Rankings"
where 2023 and AtoZRankings
sort AtoZRankings[0].ovr desc
```
