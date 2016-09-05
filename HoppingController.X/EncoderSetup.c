#include "EncoderSetup.h"

Encoder encoder = { .position = 0, .lastPosition = 0, .velocity = 0 };

void EncoderSetup()
{
    ///////////// SETUP QEI1 //////////////////////////////////////////////////////////
    QEI1CONbits.QEIEN = 0;      // Enable/Disable
    QEI1CONbits.QEISIDL = 0;    // Module runs in CPU Idle
    QEI1CONbits.PIMOD = 0;      // Index has no effect on count
    QEI1CONbits.IMV = 0;        // Phase Match Something Something
    QEI1CONbits.INTDIV = 0;     // 1:1 Clock Prescaler
    QEI1CONbits.CNTPOL = 0;     // Position/Index Counter Direction
    QEI1CONbits.GATEN = 0;      // External Gate does not effect position counter
    QEI1CONbits.CCM = 0;        // Quadrature Mode

    QEI1IOCbits.QCAPEN = 0;     // Index match does not trigger position capture
    QEI1IOCbits.FLTREN = 1;     // Filter Enable
    QEI1IOCbits.QFDIV = 0;      // 1:1 Input Filter Clock Divide
    QEI1IOCbits.OUTFNC = 0;     // Output disabled
    QEI1IOCbits.SWPAB = 0;      // Swap A/B Channels
    QEI1IOCbits.HOMPOL = 0;     // Input Invert
    QEI1IOCbits.IDXPOL = 0;     // Input Invert
    QEI1IOCbits.QEBPOL = 0;     // Input Invert
    QEI1IOCbits.QEAPOL = 0;     // Input Invert
    
    QEI1STATbits.PCHEQIEN = 0;      // Position Counter > Interrupt Disabled
    QEI1STATbits.PCLEQIEN = 0;      // Position Counter < Interrupt Disabled
    QEI1STATbits.POSOVIEN = 0;      // Position Counter Overflow Interrupt Disabled
    QEI1STATbits.PCIIEN = 0;        // Position Counter Homing Process Complete Interrupt Disabled
    QEI1STATbits.VELOVIRQ = 0;      // Velocity Counter overflow Interrupt Disabled
    QEI1STATbits.HOMIEN = 0;        // Home Input Interrupt Disabled
    QEI1STATbits.IDXIEN = 0;        // Index Input Interrupt Disabled

    QEI1CONbits.QEIEN = 1;      // Enable Encoder
}

void updateEncoderPosition()
{
    encoder.lastPosition = encoder.position;
    encoder.position += POS1CNTL;
    encoder.position += ((int32_t)(POS1CNTH) << 16);
    POS1CNTL = 0;
    POS1CNTH = 0;
}

void updateEncoderVelocitySimple()
{
    encoder.velocity = encoder.position - encoder.lastPosition;
}

