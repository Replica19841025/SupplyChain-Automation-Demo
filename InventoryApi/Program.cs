var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Your JSON files are in the folder above InventoryApi.
var dataFolder = Path.GetFullPath(
    Path.Combine(app.Environment.ContentRootPath, ".."));

app.MapGet("/", () => Results.Ok(new
{
    message = "Supply Chain Inventory API is running",
    inventory = "/api/inventory",
    shortages = "/api/shortages"
}));

app.MapGet("/api/inventory", () =>
    SendJsonFile("inventory.json"));

app.MapGet("/api/shortages", () =>
    SendJsonFile("shortages.json"));

app.Run();

IResult SendJsonFile(string fileName)
{
    var path = Path.Combine(dataFolder, fileName);

    if (!File.Exists(path))
    {
        return Results.Problem(
            title: $"{fileName} was not found",
            statusCode: 500);
    }

    return Results.File(path, "application/json");
}