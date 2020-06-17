basic.forever(function () {
    led.plotBarGraph(
    input.acceleration(Dimension.X),
    1023
    )
})
basic.forever(function () {
    led.plotBarGraph(
    input.acceleration(Dimension.Y),
    1023
    )
})
basic.forever(function () {
    if (input.acceleration(Dimension.X) < 200 && input.acceleration(Dimension.X) > -200 && (input.acceleration(Dimension.Y) < 200 && input.acceleration(Dimension.Y) > -200)) {
        pins.digitalWritePin(DigitalPin.P0, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
})
