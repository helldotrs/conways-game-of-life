for cell in maingrid:
    touch   = cell.touch
    life    = cell.life
    print('check')

    if life:
        print('life')

        if !(touch == 2 or touch == 3):
            reap()
            print ('reap()')
    elif !life:
        print('!life')

        if touch == 3:
            sow()
            print('sow()')
        else:
            print('nothing')
