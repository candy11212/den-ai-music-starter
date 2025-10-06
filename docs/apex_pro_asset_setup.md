# Apex Pro Asset Setup

This project does not bundle the `Apex Pro` asset directly. If you have received the
archive `Apex_Pro.zip` (for example at `C:\\Users\\xxvam\\Downloads\\Apex_Pro.zip` on
Windows), use the following steps to incorporate it into your working tree.

1. **Copy the archive into the repository**
   - Move `Apex_Pro.zip` to the root of your local clone of this repository.
2. **Extract the archive**
   - On Windows PowerShell:
     ```powershell
     Expand-Archive -Path .\Apex_Pro.zip -DestinationPath .\assets\apex_pro
     ```
   - On macOS or Linux:
     ```bash
     unzip Apex_Pro.zip -d assets/apex_pro
     ```
3. **Keep large assets out of version control**
   - If the extracted content is large or proprietary, add `assets/apex_pro/`
     to your `.gitignore` before committing.
   - Share the archive through your preferred storage solution instead of
     pushing it to Git.
4. **Reference the assets in your application**
   - Update configuration files or environment variables so that the frontend,
     backend, or worker services can locate the extracted files under
     `assets/apex_pro/`.

These steps ensure that collaborators can set up the required files locally
without bloating the repository or exposing licensed material.
