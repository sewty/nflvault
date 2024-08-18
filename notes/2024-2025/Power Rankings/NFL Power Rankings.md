
## Rankings Summary

```dataviewjs

dv.table(["Rank", "Team", "BottomLineRankings", "AtoZ", "Florio", "MockDraftGuy", "kimes-yates", "yates", "kimes-brandt", "brandt", "kimes-ruben", "ruben", "kimes-clark", "clark", "clong", "tps1", "tps2", "Average"],
  dv.pages('"notes/2024-2025/Power Rankings/Team Power Rankings"')
    .where(p => p.BottomLineRankings && p.AtoZ && p.Florio && p.MockDraftGuy && p.kimes && p.tps1 && p.tps2)
    .map(p => {
      let teamName = p.file.name.split('.')[0]; // Extract the team name from the file name
      let scores = [
        p.BottomLineRankings,
        p.AtoZ,
        p.Florio,
        p.MockDraftGuy,
        p.kimes[0]?.['kimes-yates'],
        p.kimes[1]?.yates,
        p.kimes[2]?.['kimes-brandt'],
        p.kimes[3]?.brandt,
        p.kimes[4]?.['kimes-ruben'],
        p.kimes[5]?.ruben,
        p.kimes[6]?.['kimes-clark'],
        p.kimes[7]?.clark,
        p.kimes[8]?.clong,
        p.tps1,
        p.tps2,
      ];
      let validScores = scores.filter(s => s !== undefined && s !== null);
      let average = validScores.reduce((a, b) => a + b, 0) / validScores.length;
      return {
        team: teamName,
        bottomLineRankings: p.BottomLineRankings,
        aToZ: p.AtoZ,
        florio: p.Florio,
        mockDraftGuy: p.MockDraftGuy,
        kimesYates: p.kimes[0]?.['kimes-yates'],
        yates: p.kimes[1]?.yates,
        kimesBrandt: p.kimes[2]?.['kimes-brandt'],
        brandt: p.kimes[3]?.brandt,
        kimesRuben: p.kimes[4]?.['kimes-ruben'],
        ruben: p.kimes[5]?.ruben,
        kimesClark: p.kimes[6]?.['kimes-clark'],
        clark: p.kimes[7]?.clark,
        clong: p.kimes[8]?.clong,
        tps1: p.tps1,
        tps2: p.tps2,
        average: parseFloat(average.toFixed(2)) // Ensure the average is a number and format to 2 decimal places
      };
    })
    .sort(p => p.average) // Sort by the Average column in ascending order
    .map((p, index) => [
      index + 1, // Rank (1-based index)
      p.team,
      p.bottomLineRankings,
      p.aToZ,
      p.florio,
      p.mockDraftGuy,
      p.kimesYates,
      p.yates,
      p.kimesBrandt,
      p.brandt,
      p.kimesRuben,
      p.ruben,
      p.kimesClark,
      p.clark,
      p.clong,
      p.tps1,
      p.tps2,
      p.average.toFixed(2) // Display the average formatted to 2 decimal places
    ])
);

```

## My Rankings
1. Chiefs - I can see this team losing a few in reg. Might struggle vs pass (no edge, lost Sneed, and meh safeties). Offense might resurge though.
2. 49ers - Will probably be the reg season standard again, at least for NFC. Pretty strong all around, but they have a tendency to lose the big games.
3. Lions - Improved Secondary. Will challenge the 49ers in postseason. Strong all around offense. Still not the strongest defense, especially down the middle, but getting better.
4. Bills - Defense healthy. Questions at WR, but the Chiefs just won a super bowl with an arguably much worse room so...
5. Texans - CJ Stroud year 2. Plenty of weapons. Looks like a solid defense
6. Ravens - Questions at OL and lost DC. It's still Lamar, but might see a bit of a regression
7. Jets - If healthy, this might be the strongest end to end team on paper.
8. Packers - Like this team. Vibes are good. Questions at LB/OL. Can they make good use of Jacobs?
9. Eagles - I don't like this team, but they're pretty stacked on paper. Still a bit sus in secondary, very reliant on young players
10. Bengals - Burrow/Chase is back. Defense looks better on paper than I gave them credit for. Running game??
11. Browns - Defense. Defense. Defense. If Watson is at least serviceable, they should be a playoff lock.
12. Dolphins - Edge players injured. If healthy, this team looks insane. If not, we'll see
13. Rams - Glass Cannon team
14. Cowboys - Uninspiring offseason. Bad vibes. LB??
15. Colts - Need AR to level up and stay healthy. I think he knows this, so I'm high on this team
16. Falcons - Lot of new faces. It's great on paper but I could see this taking a bit to really spin up. Also, edge defenders are not a thing??
17. Bucs - 
18. Steelers
19. Jaguars
20. Bears
21. Vikings
22. Chargers
23. Seahawks
24. Titans
25. Patriots
26. Broncos
27. Cardinals
28. Raiders
29. Saints
30. Giants
31. Panthers
32. Commanders

## Bootleg Football Conversions
```dataviewjs
dv.table(
  ["Rank", "Team", "2023 Rank", "Average", "Bootleg", "BottomLineRankings", "AtoZ", "Florio", "MockDraftGuy", "kimes-yates", "yates", "kimes-brandt", "brandt", "kimes-ruben", "ruben", "kimes-clark", "clark", "clong", "tps1", "tps2"],
  dv.pages('"notes/2024-2025/Power Rankings/Team Power Rankings"')
    .where(p => p.BottomLineRankings && p.AtoZ && p.Florio && p.MockDraftGuy && p.kimes && p.tps1 && p.tps2)
    .map(p => {
      let teamName = p.file.name.split('.')[0]; // Extract the team name from the file name

      // Extract the values for pwr, ceiling, and floor
      let pwr = p.bootleg[1]?.pwr;
      let ceiling = p.bootleg[10]?.ceiling;
      let floor = p.bootleg[11]?.floor;

      // Calculate the average for bootleg
      let bootlegAverage = (ceiling + floor) / 2;

      let scores = [
        p.BottomLineRankings,
        p.AtoZ,
        p.Florio,
        p.MockDraftGuy,
        p.kimes[0]?.['kimes-yates'],
        p.kimes[1]?.yates,
        p.kimes[2]?.['kimes-brandt'],
        p.kimes[3]?.brandt,
        p.kimes[4]?.['kimes-ruben'],
        p.kimes[5]?.ruben,
        p.kimes[6]?.['kimes-clark'],
        p.kimes[7]?.clark,
        p.kimes[8]?.clong,
        p.tps1,
        p.tps2,
      ];

      let validScores = scores.filter(s => s !== undefined && s !== null);
      let average = validScores.reduce((a, b) => a + b, 0) / validScores.length;

      return {
        team: teamName,
        bottomLineRankings: p.BottomLineRankings,
        aToZ: p.AtoZ,
        florio: p.Florio,
        mockDraftGuy: p.MockDraftGuy,
        kimesYates: p.kimes[0]?.['kimes-yates'],
        yates: p.kimes[1]?.yates,
        kimesBrandt: p.kimes[2]?.['kimes-brandt'],
        brandt: p.kimes[3]?.brandt,
        kimesRuben: p.kimes[4]?.['kimes-ruben'],
        ruben: p.kimes[5]?.ruben,
        kimesClark: p.kimes[6]?.['kimes-clark'],
        clark: p.kimes[7]?.clark,
        clong: p.kimes[8]?.clong,
        tps1: p.tps1,
        tps2: p.tps2,
        pwr: pwr,
        ceiling: ceiling,
        floor: floor,
        bootlegAverage: bootlegAverage,
        average: parseFloat(average.toFixed(2)) // Ensure the average is a number and format to 2 decimal places
      };
    })
    // Sort first by pwr to calculate '2023 Rank'
    .sort(p => p.pwr)
    .map((p, index, arr) => {
      p.rank2023 = index + 1;
      return p;
    })
    // Sort by bootlegAverage to calculate 'Bootleg'
    .sort(p => p.bootlegAverage)
    .map((p, index, arr) => {
      p.bootlegRank = arr.length - index; // Reverse index to rank descending by bootlegAverage
      return p;
    })
    // Final sort by the Average column
    .sort(p => p.average)
    .map((p, index) => [
      index + 1, // Rank (1-based index)
      p.team,
      p.rank2023,
      p.average.toFixed(2), // Display the average formatted to 2 decimal places
      p.bootlegRank,
      p.bottomLineRankings,
      p.aToZ,
      p.florio,
      p.mockDraftGuy,
      p.kimesYates,
      p.yates,
      p.kimesBrandt,
      p.brandt,
      p.kimesRuben,
      p.ruben,
      p.kimesClark,
      p.clark,
      p.clong,
      p.tps1,
      p.tps2
    ])
);
```
## My Rankings (8.12.24)
1. Chiefs -> its the chiefs. Running game is rising. Defense should still be solid. Hopeful WR room compared to last year
2. Lions -> Secondary was the problem. They attacked that in the offseason. Might not be a top 10 defense yet, but they moved positively. Retained the offense + OC
3. 49ers -> Still arguably the best NFL offense.
4. Ravens -> Lot of FA losses. Lot of gains (King Henry) in FA/Draft. Lost DC. I have to trend down but this is still super-bowl bound team
5. Eagles -> Secondary was the problem. They made some positive strides. Also gained Saquon.
6. Texans -> yeehaw
7. Bengals -> Burrow is back. Remember this team in 2022? They're back
8. Bills -> Defense is healthy. New running game. Questions at WR, but S+ tier QB -> this is the Chiefs recipe
9. Packers -> Young team trending up. Lot of weapons. Strong offseason in terms of defensive upgrades
10. Jets -> He just can't tear it again right? S-tier defense. Hall of Fame QB. Breeeeeece and an OLine?
11. Browns -> This team really should work...Watson??
12. Dolphins -> If they get their edges back this team gets scary. Offense should be firing again, at least for the first 10 weeks...
13. Rams -> Big offense. Glass cannon team. Maybe the DL can play above expectations?
14. Cowboys -> Awful offseason. Organizational change needed. This team can't be high on morale
15. Falcons -> No edge rush. Everything else in place
16. Bears -> Caleb looks good preseason Week 1
17. Colts
18. Steelers
19. Seahawks
20. Jaguars
21. Bucs
22. Saints
23. Cardinals
24. Titans
25. Chargers
26. Vikings
27. Raiders
28. Broncos
29. Giants
30. Commanders
31. Patriots
32. Panthers