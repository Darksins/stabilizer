def on_forever():
    led.plot_bar_graph(input.acceleration(Dimension.X), 1023)
basic.forever(on_forever)

def on_forever2():
    led.plot_bar_graph(input.acceleration(Dimension.Y), 1023)
basic.forever(on_forever2)

def on_forever3():
    if input.acceleration(Dimension.X) < 200 and input.acceleration(Dimension.X) > -200 and (input.acceleration(Dimension.Y) < 200 and input.acceleration(Dimension.Y) > -200):
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
basic.forever(on_forever3)
