/* 
 * File:   EncoderSetup.h
 * Author: JRK
 *
 * Created on April 23, 2013, 6:25 PM
 */

#ifndef ENCODERSETUP_H
#define	ENCODERSETUP_H

#include <xc.h>
#include <stdint.h>
#include "UARTSetup.h"

typedef struct Encoder
{
    int32_t position;
    int32_t lastPosition;
    int16_t velocity;
} Encoder;

extern Encoder encoder;

void EncoderSetup();
void updateEncoderPosition();
void updateEncoderVelocitySimple();

#endif	/* ENCODERSETUP_H */

