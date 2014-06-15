#include <rules.h>

streams_t* rules() {

  return new streams_t(send_index());

}
