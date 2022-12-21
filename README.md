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

> docker build
``` shell
docker build -t dotnet-webapi ./server-dotnet-webapi/.
```

> docker run
``` bash
docker run -d -p 8010 -name dotnet-webapi dotnet-webapi
```

---------------------------------------