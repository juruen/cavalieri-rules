#ifndef RULES_RULES_H
#define RULES_RULES_H

#include <streams/stream_functions.h>
#include <index/index.h>

#define EXPORT_RULES(x) streams_t* rules() { return new streams_t(x());}

extern "C" {

streams_t* rules();

}

#endif
