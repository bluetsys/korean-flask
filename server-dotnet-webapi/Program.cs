using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;

var app = WebApplication.Create(args);

app.MapGet("/", (Func<string>)(() => System.Environment.MachineName));
app.MapGet("/health", (Func<string>)(() => System.Environment.MachineName));

app.Run();