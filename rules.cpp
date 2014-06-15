#include <rules.h>

streams_t* rules() {

  auto mail_stream = email("localhost", "cavalieri@localhost",
                           "devops@localhost");

  auto s = service("requests_rate")
              >> above(40)
                >> set_state("critical")
                  >> changed_state("ok")
                    >>  mail_stream;

  return new streams_t(s);
}
