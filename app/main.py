def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print (f"Der Code ist gefälscht, es sollten 2 Schritte statt 3 sein.")
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
