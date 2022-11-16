input.onLogoEvent(TouchButtonEvent.Touched, function () {
	
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 4; index++) {
        music.playMelody("E C C5 - C5 G - G ", 500)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        music.playMelody("E C C5 - C5 G - G ", 500)
        basic.showLeds(`
            . # # # .
            # # . . .
            # . . . .
            # . . . #
            # # # # #
            `)
        music.playMelody("E C C5 - C5 G - G ", 500)
        basic.showLeds(`
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    basic.showString("Hoi Samuel")
})
