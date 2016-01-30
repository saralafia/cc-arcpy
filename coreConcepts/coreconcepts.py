# -*- coding: utf-8 -*-

from fields import *
from utils import *

class CcField(object):
    """
    Class defining abstract field.
    Based on Field.hs
    """

    def __init__(self, fieldFunction, geoObject, geoEvent):
        """ Define appropriate parameters for construction of the concrete object """
        # TODO: restrict value pairs to geoObject
        pass

    def value_at( self, position ):
        """
        @return the value of field at position, or None if it is outside of the domain.
        """
        # TODO: check if position falls within value
        raise NotImplementedError("valueAt")

    def domain( self ):
        """
        @return current domain of the field
        """
        raise NotImplementedError("domain")

    def restrict_domain(self, geometry ):
        """
        @param domain a domain to be subtracted to the current domain
        """
        raise NotImplementedError("restrict_domain")

    def rect_neigh( self, position, width, height ):
        """
        Map algebra: rectangular neighborhood function
        @return Geometry (a field mask)
        """
        raise NotImplementedError("rectNeigh")

    def zone( self, position ):
        """
        Map algebra: zone function
        @return Geometry (a field mask)
        """
        raise NotImplementedError("zone")

    def local( self, fields, fun ):
        """
        Map algebra's local operations, with a function to compute the new values
        @param fields other fields
        @return new CcField field
        """
        raise NotImplementedError("local")

    def focal( self, fields, fun ):
        """
        Map algebra's focal operations, with a kernel function to compute the new values based on the neighborhood of the position
        @return new CcField field
        """
        raise NotImplementedError("focal")

    def zonal( self, fields, fun ):
        """
        Map algebra's zonal operations, with a function to compute the new values based on zones containing the positions.
        @return new CcField field
        """
        raise NotImplementedError("zonal")

class CcObject(object):
    """
    Abstract class for core concept 'object'
    Based on Object.hs
    """

    def bounds( self ):
        raise NotImplementedError("bounds")

    def relation( self, obj, relType ):
        """ @return Boolean True if self and obj are in a relationship of type relType
                    False otherwise
        """
        raise NotImplementedError("relation")

    def property( self, prop ):
        """
        @param prop the property name
        @return value of property in obj
        """
        raise NotImplementedError("property")

    def identity( self, obj ):
        """
        @param an object
        @return Boolean True if self and obj are identical
        """
        raise NotImplementedError("identity")

class CcGranularity:
    def __init__(self):
        pass
        # TODO: cell_size_x, cell_size_y