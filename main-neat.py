for cell in maingrid:
    touch   = cell.touch
    life    = cell.life
    if life:
        if !(touch == 2 or touch == 3):
            reap()
    else:
        if touch == 3:
            sow()

