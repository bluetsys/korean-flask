> dotnet
``` cs
var app = WebApplication.Create(args);

app.MapGet("/", (Func<string>)(() => "Hello World"));
app.MapGet("/health", (Func<string>)(() => System.Environment.MachineName));

app.Run();
```

``` bat
docker build -t wymoon2690/dotnet-webapi .
docker push wymoon2690/dotnet-webapi
```