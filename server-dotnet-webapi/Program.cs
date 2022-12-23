var app = WebApplication.Create(args);

app.MapGet("/", (Func<string>)(() => "Hello World"));
app.MapGet("/health", async context =>
    {
        await context.Response.WriteAsJsonAsync(
            new
            {
                hostname = System.Environment.MachineName,
                language =
             new
             {
                 name = "dotnet",
                 version = System.Environment.Version,
             },
                web =
                new
                {
                    name = "aspnet",
                    version = System.Environment.Version,
                }
            });
    });

app.Run();