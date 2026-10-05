# Supply Chain Automation Demo: first exercise

This personal portfolio exercise uses entirely fictional parts and suppliers.
Your first goal is to read JSON inventory data, validate it using Python, identify
parts below their reorder point, and save the results in a new JSON file.

## Files

| File | Purpose |
| --- | --- |
| inventory.json | Ten fictional inventory records you can edit. |
| validate_inventory.py | Reads, validates, calculates, and saves results. |
| README.md | Instructions and practice checks. |
| shortages.json | Created or refreshed after a successful run. |

## Open and run on Windows

1. Download SupplyChain-Automation-Demo-Starter.zip.
2. In Chrome, press Ctrl+J and find that ZIP. Use its folder icon / Show in folder.
3. In File Explorer, right-click the ZIP and select Extract All, then Extract.
4. Open Visual Studio Code.
5. Select File > Open Folder. Navigate into the extracted folder and select
   SupplyChain-Automation-Demo, the folder directly containing inventory.json,
   validate_inventory.py, and README.md. Click Select Folder.
6. Select Terminal > New Terminal. In the terminal at the bottom, enter:

   ```powershell
   python --version
   ```

   If it displays Python 3.x, continue. If it does not, try `py --version`.
   If only `py` works, use `py` in place of `python` in the run command below.
   If neither works, install Python using the official instructions at
   https://docs.python.org/3/using/windows.html, close and reopen VS Code,
   reopen this project folder, and repeat this step.
7. In the left Explorer pane, click inventory.json to inspect the sample data.
   Then click validate_inventory.py to inspect the program.
8. Click in the terminal at the bottom and enter:

   ```powershell
   python validate_inventory.py
   ```

9. Read the terminal results. A new shortages.json file appears in the left
   Explorer pane after success. Click it to inspect the five flagged records.

This script uses Python's standard library. No pip packages are needed.
The Microsoft Python extension for VS Code is optional for this terminal-based
exercise; it provides editor support and a Run Python File button if installed.

## Meaning of the data

| Field | Meaning |
| --- | --- |
| partNumber | The fictional part's identifier. |
| supplier | The fictional supplier's name. |
| quantityOnHand | Units currently in stock. |
| reorderPoint | The threshold used for this exercise. |
| leadTimeDays | Sample days for a supplier to deliver; stored for later exercises. |
| gapToReorderPoint | How many units a flagged part is below its reorder point. |

Example: DEMO-101 has 12 units and a reorder point of 20, so its gap is 8 units.
This exercise flags `quantityOnHand < reorderPoint`. A part exactly at its
reorder point is not flagged in this exercise. Real replenishment policies may
trigger at equality and include on-order stock, demand, safety stock, order
quantities, and lead times. The gap here is a learning calculation, not a
complete purchase-order recommendation.

## Expected result with the original data

```text
Checked: 10 inventory records
Parts below reorder point: 5
Total gap to reorder points: 70 units

DEMO-101: on hand 12, reorder point 20, gap 8
DEMO-103: on hand 4, reorder point 15, gap 11
DEMO-105: on hand 8, reorder point 25, gap 17
DEMO-106: on hand 0, reorder point 10, gap 10
DEMO-109: on hand 6, reorder point 30, gap 24

Saved: shortages.json
```

## Practice checks

Always press Ctrl+S after editing inventory.json, then run the same command again.

1. Find DEMO-101 and change quantityOnHand from 12 to 25. Run the script.
   Expected: 4 flagged parts, total gap 62 units, and no DEMO-101 in shortages.json.
2. For that same record, temporarily change quantityOnHand to -5. Run it.
   Expected: an ERROR explaining that quantityOnHand must be 0 or more. Results
   are not refreshed while the input is invalid. Restore it to 12 and rerun.
3. Temporarily make that record's partNumber an empty string, `""`. Run it.
   Expected: an ERROR that partNumber must contain text. Restore DEMO-101 and rerun.
4. Inspect the Python file's five numbered comments. Connect each comment to the
   input file, validation checks, calculation, output file, or displayed result.

After restoring the original data, you should again see 5 flagged parts and 70 units.

## Next project stages

1. Record changes using Git and publish the project to GitHub.
2. Build a small C# / ASP.NET Core inventory API.
3. Test the API using Postman.
4. Connect a C# / Blazor dashboard to the API.
5. Add SQL storage and document the data checks and migration.

Only add these skills to your resume as you actually implement and verify them.

## Official setup references

- https://code.visualstudio.com/download
- https://docs.python.org/3/using/windows.html
- https://code.visualstudio.com/docs/python/python-quick-start
- https://code.visualstudio.com/docs/terminal/getting-started

## Run the complete demo locally

Requires Python 3 and the .NET 10 SDK.

Run all commands from the main SupplyChain-Automation-Demo folder.

### 1. Validate inventory

```powershell
py validate_inventory.py
```

This generates shortages.json from inventory.json.

### 2. Start the C# API

```powershell
dotnet run --project InventoryApi --no-launch-profile --urls http://localhost:5050
```

Leave this terminal running.

### 3. Start the Blazor dashboard in a second terminal

```powershell
dotnet run --project InventoryDashboard --no-launch-profile -- --urls http://localhost:5051 --environment Development
```

Open http://localhost:5051 in your browser.

### Update the data

Edit inventory.json, save it, and run the Python validator again.
Click Refresh data on the dashboard to load the updated results.

### API endpoints

- GET /api/inventory — all inventory records
- GET /api/shortages — parts below their reorder points

Both endpoints were manually checked in Postman and returned 200 OK.

### Scope

This portfolio demo uses fictional data stored in local JSON files.
The gap measures units below reorder thresholds, not a full recommended
order quantity. The dashboard currently runs locally.