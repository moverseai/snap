# snap

1. `hugo.exe new site page`
2. `cd page`
3. `hugo.exe mod init github.com/moverserai/snap`
4. create `configs/_default/module.toml`
   ```toml
   [[imports]]
   disable = false
   path = "github.com/nunocoracao/blowfish/v2"
   ```
5. add `go` module to `go.mod`
    ```go
    require github.com/nunocoracao/blowfish/v2 v2.78.0 // indirect
    ```