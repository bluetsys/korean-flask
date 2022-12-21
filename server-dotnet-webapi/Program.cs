var app = WebApplication.Create(args);

app.MapGet("/", (Func<string>)(() => "Hello World"));
app.MapGet("/health", (Func<string>)(() => System.Environment.MachineName));

app.Run();