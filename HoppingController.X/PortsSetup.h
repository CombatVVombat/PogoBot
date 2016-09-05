#ifndef PORTSSETUP_H
#define	PORTSSETUP_H

#include <xc.h>
#include "PPS.h"

#define MOTOR_CTRL_A LATBbits.LATB11
#define MOTOR_CTRL_B LATBbits.LATB10

void PortsSetup();

#endif	/* PORTSSETUP_H */

