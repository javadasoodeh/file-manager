import math

__author__ = 'javadasoodeh73@gmail.com'


class FileUtils:
    """
        human_readable_byte_count() function
        output example :

                                         SI       BINARY

                               0:        0 B        0 B
                              27:       27 B       27 B
                             999:      999 B      999 B
                            1000:     1.0 kB     1000 B
                            1023:     1.0 kB     1023 B
                            1024:     1.0 kB    1.0 KiB
                            1728:     1.7 kB    1.7 KiB
                          110592:   110.6 kB  108.0 KiB
                         7077888:     7.1 MB    6.8 MiB
                       452984832:   453.0 MB  432.0 MiB
                     28991029248:    29.0 GB   27.0 GiB
                   1855425871872:     1.9 TB    1.7 TiB
             9223372036854775807:     9.2 EB    8.0 EiB
    """

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def human_readable_byte_counts(bytes_, si):
        unit = 1000 if si else 1024
        if bytes_ < unit:
            return str(bytes_) + " B"
        exp = int((math.log(bytes_) / math.log(unit)))
        pre = ("kMGTPE" if si else "KMGTPE")[(exp - 1)] + ("" if si else "i")
        return "%.1f %sB" % (bytes_ / math.pow(unit, exp), pre)
