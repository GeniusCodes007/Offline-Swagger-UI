"""
First:Download the zip file containing the swagger ui files from https://github.com/swagger-api/swagger-ui/archive/refs/tags/v5.17.14.zip or

    Download the one provided here

Second: Extract or Unzip the contents of the zip file into your project folder and create a folder 'docs' in your project folder

Third: Copy all contents of the directory 'dist' into the 'docs' folder.

Fourth: Create a Python file 'dump_spec.py' in your project folder

Fifth: Input the code:

        import json

        from main import app # replace 'main' with name of the Python file containing your application, and

        # 'app' with the name of the application instance

        with open('docs/openapi.json', 'w') as json_file: # You replace 'json_file' with any string of your choice

            json.dump(app.openapi(), json_file, indent=2)

        print('Created openapi.json in your project folder')

Sixth: Run the command:

        python dump_spec.py

Seventh: You're done and good to go!



"""